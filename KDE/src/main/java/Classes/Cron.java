/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.KDE.Classes;

import BD.ChaveSessao;
import BD.Configuracoes;
import BD.Log;
import java.io.IOException;
import java.util.Calendar;
import java.util.Date;
import java.util.Objects;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

/**
 * Se atividade diferente, cria nova atividade.
 * Se atividade iguais, atualiza só a data fim.
 * Se atividades iguais e nova sessão, cria nova atividade. (Como saber se é nova sessão?)
 * @author leonardo
 */
public class Cron {
    
    /**
     *
     */
    public void Cron(){
      //  Date now;
     //   String nowString;
        Date data_fim_log_data; // Data do log em formato Date para usar quando precisar somar loop.
        String data_fim_log;
        String data_inicio_log;
        Date data_sistema;
        
        String nome_atividade_log;
        String nome_atividade_sistema;
        String chave_sessao;
        String chave_ultimo_log;
        
        // não usar loop, pois só usa na classe atividade.
    //    int loop_configuracao; // Vem das configurações.
     //   int loop; // informa se cria a data com ou sem o loop.
        
            // Contruíndo objetos
            Atividade atividade = new Atividade();
            TratarData tratardata = new TratarData();
          //  Configuracoes configuracoes = new Configuracoes();
           // ChaveSessao chavesessao = new ChaveSessao();
    
                // Consultando base e preenchendo objetos
                EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
                EntityManager em = emf.createEntityManager();
                Log logz = em.find(Log.class, atividade.PegarIdUltimaAtividadeLog()); 
                Configuracoes configuracoes = em.find(Configuracoes.class, 1); // configuracoes só deve ter ID 1.
                ChaveSessao chavesessao = em.find(ChaveSessao.class, 1); // só deve ter ID 1.
                
                
// TODOS OS DADOS JÁ DEVEM ESTAR CARREGADOS ANTES DE INICIAR O LOOP            
            // LOOP e CHAVE
            //    loop_configuracao = configuracoes.getLoop();
                //TESTE CHAVE - COMENTE E DESCOMENTE A LINHA PARA FIXAR A CHAVE. Tem
                chave_sessao = chavesessao.getChave();
              //  chave_sessao = logz.getChaveSessao();
                
                         
                chave_ultimo_log = logz.getChaveSessao();
             //   System.out.println("looooooooop"+loop_configuracao);
                    
                // NOME ATIVIDADES
                    nome_atividade_log = logz.getAtividade();
                        try {
                    nome_atividade_sistema = atividade.PegarAtividadeSistema();
                        } catch (IOException | InterruptedException iOException) {
                            nome_atividade_sistema = "ERRO AO PEGAR LER ATIVIDADE DO SISTEMA";
                        }
                            // COLETA DATAS DO LOG E SISTEMA - tem que estar em formato Date para retirar os minutos
                            Calendar calendario = Calendar.getInstance();
                                // DATAS e STRINGS 
                                     // DATA SISTEMA - usar com ou sem loop
                                       data_sistema = tratardata.DataSistemaData(0);
                                    // DATA__INICIO log
                                        data_inicio_log = logz.getInicio();
                                    // DATA_FIM log
                                        data_fim_log = logz.getFim(); //STRING
                                        data_fim_log_data = tratardata.DataStringParaData(data_fim_log); //DATE
                                       


                                            // FORMATAR SÓ PARA DATA (dd-mm-aaaa)
                                             //   nowString = tratardata.PegarSoData(now);
                                             //   data_fim = tratardata.PegarSoData(data_fim_data); 
                                             

                                            
// ROTINAS IF
    // TODOS OS DADOS JÁ DEVEM ESTAR CARREGADOS ANTES DE INICIAR O LOOP
    // TODOS OS IFS TÊM QUE ESTAREM ANINHADOS. Se tiver algum solto, pode dar problema.

    
///CHAVES log e sistema para ver se log é da sessão atual.
    if (!Objects.equals(chave_sessao, chave_ultimo_log)) {
        System.out.println("chaves diferentes - cria atividade");
        atividade.CriarAlterarAtividade(atividade.PegarIdUltimaAtividadeLog(), nome_atividade_sistema, tratardata.DataSistemaParaString(0), tratardata.DataSistemaParaString(0), 1, 1);
    }else{ 
        System.err.println("chaves iguais");
        
        ///DATAS diferentes, já cria a atividade. - Já trata problema se passar da meia noite, pois se data difere, cria atividade
            if (!Objects.equals(tratardata.PegarSoData(data_sistema).trim(),tratardata.PegarSoData(data_fim_log_data).trim())) {
                System.out.println("datas diferentes - cria atividade");
              atividade.CriarAlterarAtividade(atividade.PegarIdUltimaAtividadeLog(), nome_atividade_sistema,  tratardata.DataSistemaParaString(0),  tratardata.DataSistemaParaString(0), 1, 1);
                    }else{
                        System.out.println("datas iguais");

                        ///NOMES atividades diferentes, cria uma atividade
                               if (!atividade.CompararAtividades()) {  
                                   System.out.println("nomes diferentes - Cria atividade");
                                   atividade.CriarAlterarAtividade(atividade.PegarIdUltimaAtividadeLog(), nome_atividade_sistema, tratardata.DataSistemaParaString(0), tratardata.DataSistemaParaString(0), 1, 1);
                               }else{
                                   System.out.println("nomes iguais - Altera atividade");
                        ///NOMES iguais - Só altera a atividade, mantendo a data inicial e atualizando a data final
                                        // aqui é diferente ao pegar data inicial do último registro e final do sistema. - NÃO USA O LOOP
                                        System.out.println(data_inicio_log);
                                        atividade.CriarAlterarAtividade(atividade.PegarIdUltimaAtividadeLog(), nome_atividade_sistema, data_inicio_log, tratardata.DataSistemaParaString(0), 0, 0);
                                    }
                }
                    // se atividades forem iguals, verifica se é nova sessão.
                    // nova sessão é quando o tempo entre as atividades     
                    
             }
            
      //  }else{System.out.println("datas iguais");}

             
             
                    
                    
}}
