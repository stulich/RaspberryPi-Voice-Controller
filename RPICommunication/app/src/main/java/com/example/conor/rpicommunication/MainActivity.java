package com.example.conor.rpicommunication;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.os.StrictMode;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    TextView res;
    int port = 25571;
    String addr ="10.0.1.5";
            //"128.119.29.26";
    //"128.119.22.155


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // allow network commands to run on main thread, create then set to policy
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
    }


    //function to be run when the button to start speech is clicked
    public void onButtonClick(View view) {
        //check to see if it is button for speech
        if (view.getId() == R.id.button) {
            //set TextView element to the input dispay, to set it to voice command
            res = (TextView) findViewById(R.id.input_display);
            //start speech function
            promptSpeech();

        }

    }


    public void promptSpeech() {
        //set up input for speech
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Say a control!");
        //try catch surrounding the creation of voice input, older android kits may not suport it
        try {
            startActivityForResult(intent, 100);

        }
        catch(ActivityNotFoundException a){
            //display error message to user if voice recognition not supported
            Toast.makeText(MainActivity.this, "Voice Recognition not supported", Toast.LENGTH_SHORT);
        }

    }


    public void onActivityResult(int req_code, int res_code, Intent i){
        super.onActivityResult(req_code, res_code, i);
        //if prooper input code for voice
        switch(req_code){
            case 100: if(res_code == RESULT_OK && i != null){
                ArrayList<String> result_arrlist = i.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                // set text to what was said
                res.setText(result_arrlist.get(0));
                //create new client to send immediately
                Client c = new Client(addr, port);
                // only send if its not empty
                if(!res.getText().equals("")){
                    c.sendString(res.getText().toString());

                }
                //exit
            }break;
        }

    }

}

