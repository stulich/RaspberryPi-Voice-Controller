package com.example.conor.rpicommunication;

import android.os.AsyncTask;
import android.widget.Toast;

import java.io.DataOutputStream;
import java.net.Socket;
import java.io.IOException;


/**
 * Created by conor on 11/4/17.
 */

public class Client extends AsyncTask<Void,Void,Void> {

    int dest_port;
    String dest_addr;
    String response = "";
    Socket socket = null;


    Client(String addr,int port){
        dest_port = port;
        dest_addr = addr;
    }


    @Override
    protected Void doInBackground(Void... arg0){
        try{
            socket = new Socket(dest_addr, dest_port);
        }
        catch(IOException io){
            io.printStackTrace();
        }
        return null;
    }

    public void sendString(String msg){
        try{
            socket = new Socket(dest_addr, dest_port);
            if(socket.isConnected()) {
                try {
                    DataOutputStream out_str = new DataOutputStream(socket.getOutputStream());
                    out_str.writeUTF(msg);
                    socket.close();
                } catch (IOException io) {
                    io.printStackTrace();
                }
            }
        }
        catch(IOException io){
            io.printStackTrace();
        }


    }


}
