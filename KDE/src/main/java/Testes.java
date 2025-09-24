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
import com.KDE.Classes.TratarData;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;



/**
 *
 * @author leonardo
 */
public class Testes {
            public Testes() throws InterruptedException{
                    Iniciar iniciar = new Iniciar();
                    
                 
     //   Atividade atividade = new Atividade();
      //  atividade.CriarAlterarAtividade(18, "dfssd", "dsfsdf", "sdfsd", 1, 1);
      EntityManagerFactory emf = Persistence.createEntityManagerFactory("MYSQL");
      EntityManager em = emf.createEntityManager();
      Configuracoes configuracoes = em.find(Configuracoes.class, 1);
      
      //  for (int i = 0; i < configuracoes.getLoop(); i++) {
            int i = 1;
        while (true) {            
            System.out.println("»»»»»»"+i+"««««««"); 
            i ++;
            Thread.sleep(60000);  // 1 segundo é 1000 milisegundos. 1 minuto é 60000 milisegundos
            
                  Cron cron = new Cron();
                     cron.Cron();
     
        
        
        
                // rotina de iniciar o sistema
            //    Iniciar iniciar = new Iniciar();


               // final String key2 = key;
                
             //   System.out.println(key);
              //  System.out.println(key);
             //   System.out.println(key);

              //  System.out.println(chave_sessao);
    //   Cron cron = new Cron();
     //   cron.Cron();
      //  Testes testes = new Testes();
    
}
             

}
}