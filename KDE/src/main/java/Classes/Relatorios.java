/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.KDE.Classes;

import BD.Log;
import java.time.Duration;
import java.util.Date;
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.TypedQuery;

/**
 *
 * @author leonardo
 */
public class Relatorios {
            String teste = "teste";
            
    public Relatorios(){

        
        
    }
    
    public void Consolidado(){
        System.out.println("relatório----------------------------------");
      EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
      EntityManager em = emf.createEntityManager();
      
      
      // LISTAS - https://www.alura.com.br/conteudo/java-collections
        TypedQuery<Log> query =
      em.createNamedQuery("Log.findAll", Log.class);
        List<Log> logzLista = query.getResultList();
        // ver se tem que preencher a lista com .add ou se já está preenchida.
        // ver sobre namedquerys
        System.out.println("Relatório: "+logzLista.get(1).getAtividade());
        
        
        
        // converte as datas para Date
        // tenta somar só as horas.
        int i=0;
        for (Log result : logzLista) {       
            System.out.println("Relatório: "+logzLista.get(i).getId());
            System.out.println("-------: "+logzLista.get(i).getAtividade());
            System.out.println("-------: "+logzLista.get(i).getInicio());
            System.out.println("-------: "+logzLista.get(i).getFim());
            System.out.println("-------: "+logzLista.get(i).getChaveSessao());
             i=i+1;
//        }      
  
    }
        
        

        
    
}}
