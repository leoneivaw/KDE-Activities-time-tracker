/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.KDE.Classes;


import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 *
 * @author leonardo
 */
public class TratarData {

    /**
     * int loop - Enviar zero para não somar loop ao tempo
     * @param loop
     * @return
     * APOSENTADO USAR DataDataParaString
     */
    public String DataSistemaParaString(int loop_config){ // PARA NÃO SOMAR LOOP, ENVIAR ZERO
                    String data_string="";
                //    System.out.println("Recebido: "+loop);
               // "dd/MM/yyyy HH:mm:ss"
              // pegando data, tranformando no pattern definido e printando ainda em formato data.
             //  SimpleDateFormat formatador = new SimpleDateFormat("EEE, d MMM yyyy HH:mm:ss Z");  

               Calendar calendario = Calendar.getInstance();
                  Date now = calendario.getTime();
                  //  System.out.println("now: "+now);
                      calendario.add(Calendar.SECOND, loop_config); // somando com loop
                        Date data_somada = calendario.getTime();
                  //      System.out.println("com loop"+calendario.getTime());


                // Pegando data do sistema e tranformando no pattern definido e tranformando em String
                SimpleDateFormat formatador = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss");
                data_string = formatador.format(data_somada);
                 //   System.out.println("data em string: "+data_string);

    return data_string;    
}
    
    
       public Date DataSistemaData(int loop){ // PARA NÃO SOMAR LOOP, ENVIAR ZERO
                    
                //    System.out.println("Recebido: "+loop);
               // "dd/MM/yyyy HH:mm:ss"
              // pegando data, tranformando no pattern definido e printando ainda em formato data.
             //  SimpleDateFormat formatador = new SimpleDateFormat("EEE, d MMM yyyy HH:mm:ss Z");  

               Calendar calendario = Calendar.getInstance();
                  Date now = calendario.getTime();
                  //  System.out.println("now: "+now);
                      calendario.add(Calendar.SECOND, loop); // somando com loop
                        Date data_somada = calendario.getTime();
                  //      System.out.println("com loop"+calendario.getTime());


                // Pegando data do sistema e tranformando no pattern definido e tranformando em String
              //  SimpleDateFormat formatador = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss");
              //  now = formatador.format(data_somada);
                 //   System.out.println("data em string: "+data_string);

    return data_somada;    
}

    /**
     * int loop - Enviar zero para não somar loop ao tempo
     */
    public Date DataStringParaData(String dataS){
             
                        // creio que só dá para formatar uma data se passar para String. Não faz sentido formatar uma data Data, pois ela tem que ficar inteira.

                             Date dataD;
                        try {
                            dataD = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss").parse(dataS);
                        } catch (ParseException ex) {
                            Logger.getLogger(TratarData.class.getName()).log(Level.SEVERE, null, ex);
                            System.out.println("ERRO NO FORMATO DA DATA\n ERRO NO FORMATO DA DATA");
                            Calendar calendario = Calendar.getInstance();
                            dataD = calendario.getTime();
                        }
    return dataD;
    }
    
    
    public String DataDataParaString(Date data){
    
                    DateFormat formatador = new SimpleDateFormat("yyyy-mm-dd hh:mm:ss");  
                    String dataString = formatador.format(data);  
                    System.out.println(dataString);
    return dataString;
    }
    
    /**
     * Recebe uma data e retorna uma String
     * @param data
     * @return 
     */
    public String PegarSoData(Date data){
                    String dataS;     
                    SimpleDateFormat formatador = new SimpleDateFormat("dd-MM-yyyy");
                    dataS = formatador.format(data);

                     //   System.out.println(data);
    return dataS;    
    }




}
