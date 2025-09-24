/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.KDE.Classes;

import BD.ChaveSessao;
import BD.Log;
import java.util.Objects;
import java.util.Random;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;

/**
 *
 * @author leonardo
 */
public final class Iniciar {
    
    
    /// não precisava criar chave de sessão se tivesse descoberto antes:  getRuntime()
    public String GerarChaveSessão() throws InterruptedException{
       String key="@";
            
            EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
            EntityManager em = emf.createEntityManager(); 
            ChaveSessao chavesessao = new ChaveSessao();
       
      
// gerando chave aleatória
            Random r = new Random();
            String alphabet = "0123456789abcdefghijklmnopqrstuvxyz%$#";
            for (int i = 0; i < 10; i++) {
            key += alphabet.charAt(r.nextInt(alphabet.length())); 
            }
// salvando chave de sessão no banco
            System.out.println(key);
            chavesessao.setChave(key);
            chavesessao.setId(1);
            em.getTransaction().begin(); 
            em.merge(chavesessao);
            em.getTransaction().commit();
             
            System.out.println(key);
        
                emf.close();
            return key;
    } 
            
    public void ValidaChave(String key) throws InterruptedException{
        
         // Checa se chave é zero. Se for, volta mensagem de inconsistência e fecha
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
        EntityManager em = emf.createEntityManager();  
        Atividade atividade = new Atividade();
       
       
        ChaveSessao chavesessao = em.find(ChaveSessao.class, 1);
        Log logz = em.find(Log.class, atividade.PegarIdUltimaAtividadeLog());

    /// checa se chaves são iguais. se forem, há outra instância aberta e encerra esta instância.    
        System.out.println("Comparar chaves");
        System.out.println(chavesessao.getChave()+"\n"+logz.getChaveSessao());
        
        if (Objects.equals(chavesessao.getChave(),logz.getChaveSessao())) {
            System.out.println("ERRO!!!\n Há outra instância aberta deste aplicativo.\n ENCERRANDO O PROGRAMA...");
                        
             Thread.sleep(10000);                 
             System.exit(0);
        }
        

        if (chavesessao.getChave().equals("0")) {
            System.out.println("Inconsistência na chave de sessão. \nVerifique se não existe outra instância aberta.\nENCERRANDO O PROGRAMA...");
            
             Thread.sleep(10000);                 
             System.exit(0);
            
        }else{ 
            
            
        }
        
        emf.close();
    }
    
    
    public void BDVazio(){ 
      int ID_log;
            EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
            EntityManager em = emf.createEntityManager(); 
            try { ////// primeira coisa a executar verificando banco vazio.
     
                            // Pega o último ID
                              Query max_id = null;
                                 // em.createNativeQuery("SELECT MAX(ID) from Log");           
                                  max_id = em.createNativeQuery("SELECT MAX(ID) from Log");  
                                  System.out.println("BDVazio"+max_id);
                                  ID_log =  (int) max_id.getSingleResult(); 
                                 // System.out.println(ID_log);
        } catch (Exception e) {
            Atividade atividade = new Atividade();
            System.out.println("Banco de dados vazio. \n Inserindo informações.");
            TratarData tratardata = new TratarData();
            atividade.CriarAlterarAtividade(1,"nome atividade", tratardata.DataSistemaParaString(0), tratardata.DataSistemaParaString(0), 2, 0);


        }
            emf.close();
    }}