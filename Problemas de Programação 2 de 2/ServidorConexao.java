import java.net.*;
import java.io.*;
import java.util.*;


public class ServidorConexao extends Thread{
    private int porta;
    private ServerSocket ouvido;
    private ObjectOutputStream output; //fluxo de saida de dados
    private ObjectInputStream inStream; //fluxo de entrada de dados

    private Vector <Servidor> listaServidor = new Vector <Servidor> ();
    private Servidor visitante;

    public void conecta (int porta){
        this.porta = porta;
        try {
            this.ouvido = new java.net.ServerSocket(porta);
        } catch (java.io.IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
        System.out.println("Servidor no ar na porta " + porta);
    }
    public ServidorConexao (String n, int gate){
        setName(n);
        conecta(gate);
    }

    public void run () {
        while (true){
            try {
                //Servidor.accept() // espera por um cliente
                visitante = new Servidor(ouvido.accept());
                if (visitante ==null)
                    System.out.println("Morreu Aqui");
                visitante.start();
                addServidor(visitante);

                visitante.informe("Bem vindo a porta: " + porta);
                visitante.informe("[Nome?]");
                //Pega os dados dos clientes e manipula a mensagem
            } catch (java.io.IOException e) {
                
            }
        }
    }
    public static void main(String[] args){
        ServidorConexao s  = new ServidorConexao("contador", 5555);
        s.start();

        ServidorConexao s2 = new ServidorConexao("cont",6666);
        s2.start();
    }
    
    private void removeServidor(Servidor j){
        listaServidor.remove(j);
    }
    private void addServidor(Servidor j){
        listaServidor.add(j);
    }

    public class Servidor extends Thread {
        private ObjectOutputStream output;  //fluxo de saida de dados
        private ObjectInputStream inStream; //fluxo de entrada de dados
        private Socket connection;          //armazena ponteiro para o servidor

        private boolean noAr = true;
        private String nome = "";
        
        public Servidor (Socket s){
            this.connection = s;            
            try {
                output = new ObjectOutputStream(s.getOutputStream());
                //cria fluxo de saida de dados
                inStream = new ObjectInputStream(s.getInputStream());
                 //cria fluxo de entrada de dados
                 output.flush();
            } catch (IOException e) {}
        }
        public void run (){
            String fofoca;
            int x;
            while (noAr){
                fofoca = ouvir(false);
                x = fofoca.indexOf("Bye");
                if (x >=0 ){
                    this.noAr = false;
                    this.interrupt();
                    ServidorConexao.this.removeServidor(this);// removia o jogador do programa
                    System.out.println("Pedido de exclusão recebido!");
                    informe("[conte mais]");
                    continue;
                }
                if (fofoca.indexOf("[nome?]")> -1){
                    nome = fofoca.substring(7);
                }
            }

        }
        
        public void informe(String m){
            try {
                output.writeObject(m);
            } catch (java.io.IOException e) {
                System.out.println("Erro de enviar de mensagem");
                this.closeConnection ();
                noAr = false;
            }

        }
        private String ouvir (boolean eco){
            String saida = new String("");
            try {
                saida = String.valueOf(inStream.readObject());
                if (eco)
                    System.out.println("ouvi " + saida);
            } catch (IOException e) {
                saida = "";
            } catch(java.lang.ClassNotFoundException clerr){
                System.out.println (clerr);
            } catch (NullPointerException err){}
            return saida;
        }
        private void closeConnection (){
            try {
                ServidorConexao.this.removeServidor(this);
                if (this.isAlive()){
                    this.interrupt();
                    connection.close();
                }
            } catch (Exception exp){
                System.out.println("Cliente ausente");
            }
        }  
   }

}
