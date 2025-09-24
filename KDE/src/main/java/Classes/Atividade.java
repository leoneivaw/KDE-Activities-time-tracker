/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.KDE.Classes;

import BD.ChaveSessao;
import BD.Configuracoes;
import BD.Log;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;


/**
 *
 * @author leonardo
 */
public class Atividade {
    
    /**
     *
     */
    public Atividade(){

    }
    
    
    /**
     *
     * @return
     * @throws IOException
     * @throws InterruptedException
     */
    public String PegarAtividadeSistema() throws IOException, InterruptedException{

        // qdbus org.kde.ActivityManager /ActivityManager/Activities ActivityName b6a18749-1ba5-4ddb-98d9-c487f6528915
        String command1 = "qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity";
        Process processo1 = Runtime.getRuntime().exec(command1);

        BufferedReader reader1 =  
              new BufferedReader(new InputStreamReader(processo1.getInputStream()));
        String ID_atividade_sistema = reader1.readLine();
        processo1.waitFor();
            
        
        String command2 = "qdbus org.kde.ActivityManager /ActivityManager/Activities ActivityName"+" "+ID_atividade_sistema;
        Process processo2 = Runtime.getRuntime().exec(command2);

        BufferedReader reader2 =  
              new BufferedReader(new InputStreamReader(processo2.getInputStream()));      
        String atividade_sistema = reader2.readLine();
        processo2.waitFor();

        return atividade_sistema;
    }
    
    /**
     *
     * @return
     */
    public int PegarIdUltimaAtividadeLog(){
               int ID_log;
      EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
      EntityManager em = emf.createEntityManager();
      
      // Pega o último ID
        Query max_id = null;
           // em.createNativeQuery("SELECT MAX(ID) from Log");
           
            max_id = em.createNativeQuery("SELECT MAX(ID) from Log");  
            ID_log =  (int) max_id.getSingleResult(); 
       
       // pega o resultado
       // trata para evitar erro se BD estiver vazio
           
        return ID_log;        
        
    }

    /**
     *
     * @return
     */
    public boolean CompararAtividades(){
        
                Atividade atividade = new Atividade();
                String atividade_sistema = "";
                String atividade_log = "";
                boolean atividades_sao_iguais;
                try {
                    atividade_sistema = atividade.PegarAtividadeSistema();
                    
                    
                    //   System.out.println("Atividade Sistema: "+atividade_sistema);
                } catch (IOException ex) {
                    Logger.getLogger(Testes.class.getName()).log(Level.SEVERE, null, ex);
                } catch (InterruptedException ex) {
                    Logger.getLogger(Testes.class.getName()).log(Level.SEVERE, null, ex);
                }
                
                System.out.println("Atividade Sistema: "+atividade_sistema);
                /////////////////////////////////////////////////////////////////
               // System.out.println("teste reg log: "+atividade.PegarAtividadeLog());
                              
                    EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
                    EntityManager em = emf.createEntityManager();
                    Log logz = em.find(Log.class, atividade.PegarIdUltimaAtividadeLog()); 
                    System.out.println(logz.getId());
                    atividade_log = logz.getAtividade();
                    
                    
                    /////////////////////////////////////
                    // compara as atividades
                 //   System.out.println(atividade_log);
                  //  System.out.println(atividade_sistema);
                    if (atividade_sistema.equals(atividade_log)) {
                        System.out.println("Atividades iguais");
                        atividades_sao_iguais = true;
                } else{
                        System.out.println("Atividades diferentes");
                        atividades_sao_iguais = false;
                    }
                    
    return atividades_sao_iguais;
    }
  
        
/** <b>DESCRIÇÃO</b> <br>
        * criar_ou_alterar - 1 cria, 0 altera, 2 Cria sem somar ID, usado só no BDVazio<br>
        * <br>
        * <b>PERSISTIR COM JPA</b>
        * em.persist(logz); PARA INSERIR<br>
        * em.merge(logz); PARA UPDATE<br>
     * @param ID_atividade - Se altera, soma +1 no ID
     * @param nome_atividade
     * @param atividade_now - Data sistema
     * @param data_inicio - Data sistema ou do log, dependendo da condição.
     * @param criar_ou_alterar - 0 altera, 1 cria, 2 cria sem somar um no ID, usado no BDVazio.
     * @param loop - 0 não usa loop, 1 usa loop
*/
    public void CriarAlterarAtividade(int ID_atividade,String nome_atividade, String data_inicio, String data_fim, int criar_ou_alterar, int loop){
            
        System.out.println(data_inicio+" from criar atividade");
        int loop_config;  
    //    String data_fim_sistema = ""; // Se receber usar_loop_data_fim acrescenta o loop
        
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
        EntityManager em = emf.createEntityManager();     
        
       
        System.out.println(ID_atividade);
        System.out.println(loop+"5555555");
        // pega configuração do tempo de loop
        TratarData tratardata = new TratarData();
        if (loop < 1) { // não usa loop
            data_fim = tratardata.DataSistemaParaString(0);
            System.out.println("loop zero");
            }if (loop > 0) { // usa loop
                System.out.println("loop maior que zero");            
            Configuracoes configuracoes = em.find(Configuracoes.class, 1); // id 1 pq só tem um único registro na tabela
            loop_config = configuracoes.getLoopz();
            System.out.println("looppppppiiii"+loop);
            System.out.println(loop_config+"loop_config");
            System.out.println(data_fim);
            System.out.println("loop"+loop);         
            data_fim = tratardata.DataSistemaParaString(loop_config); // Se quiser a data sem somar loop, passar zero    
            System.out.println(data_fim);
            }if (loop > 1) { // não usa loop
               
                System.out.println("ERRO - VALOR INVÁLIDO PARA O LOOP");
            }
        
        System.out.println(ID_atividade);    
       //////BUG WORKROUND - TRATANDO O BUG //////////
       //  Log logz = new Log(null, atividadeNow, data_inicio, data_fim_sistema); // BUG, NÃO INSERE SE DEIXAR NULO.
        if ((criar_ou_alterar == 1) || (criar_ou_alterar == 2) ) {
            // insere
         //   System.out.println(ID_atividade);
            if (criar_ou_alterar == 1) {
                ID_atividade=ID_atividade+1;
            }
            // ID = 0
           // System.out.println(ID_atividade);

        } else{
            // altera atividade. Sem ação, pois o id continua o mesmo.
            
        }
        
        // trata data

        ChaveSessao chavesessao = new ChaveSessao();
        chavesessao = em.find(ChaveSessao.class, 1);

        System.out.println("key: "+chavesessao.getChave());
        System.out.println(nome_atividade);
        System.out.println(data_inicio);
        System.out.println(data_fim);
        Log logz = new Log(ID_atividade, nome_atividade, data_inicio, data_fim, chavesessao.getChave()); // BUG, NÃO INSERE SE DEIXAR NULO.
        System.out.println("ID: "+logz.getId()+"\nATV: "+logz.getAtividade()+"\nDataInício: "+logz.getInicio()+"\nDataFim:    "+logz.getFim());
     
        em.getTransaction().begin(); 
        // MERGE PARA UPDATE REGISTRO
        // PERSISTE PARA INSERIR
        if (criar_ou_alterar == 1) {
            em.persist(logz);
        }else{
        em.merge(logz);
        }
        em.getTransaction().commit();
        emf.close();  
      
    
}
}
