/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.KDE;

import BD.Configuracoes;
import com.KDE.Classes.Atividade;
import com.KDE.Classes.Cron;
import com.KDE.Classes.Iniciar;
import com.KDE.Classes.Relatorios;
import static java.lang.Runtime.getRuntime;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;




public class KDEActivities {
    
  
    public static void main(String[] args) throws InterruptedException {

        System.out.println("Hello World!!!");
        Iniciar iniciar = new Iniciar();
    //    String key = iniciar.GerarChaveSessão();
       //iniciar.ValidaChave(key);
        iniciar.BDVazio(); 
        
        
       
      //  Relatorios relatorios = new Relatorios();
      //  relatorios.Consolidado();
        
        
        
        Testes testes = new Testes();
        
}}
