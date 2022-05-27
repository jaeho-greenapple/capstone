package edu.lesson.webcamera;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.util.Log;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.twilio.Twilio;
import com.twilio.converter.Promoter;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

import java.net.URI;
import java.math.BigDecimal;

/*public class Example {
    // Find your Account Sid and Token at twilio.com/user/account
    public static final String ACCOUNT_SID = "ACf5245c20b049be1e29763df5d6389563";
    public static final String AUTH_TOKEN = "8e4cae83eaf081f23b935fa99b11497f";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);

        Message message = Message.creator(new PhoneNumber("+8201056294406"),
                new PhoneNumber("+8201056294406"),
                "This is the ship that made the Kessel Run in fourteen parsecs?").create();

        System.out.println(message.getSid());
    }
}*/
public class cctvActivity extends AppCompatActivity {
    final String TAG = "TAG+CCTVFragment";
    Button cctvOnButton, cctvOffButton, cctvCenterButton, cctvLeftButton, cctvRightButton;
    WebView webView;
    WebSettings webSettings;
    TextView callText;
    WebView webView_2;

    @SuppressLint({"ClickableViewAccessibility", "SetJavaScriptEnabled"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cctv);

        Log.d(TAG,"Create CCTV Fragment");

        webView = (WebView) findViewById(R.id.cctvWeb);
        callText = (TextView) findViewById(R.id.callText);
        webView_2= (WebView) findViewById(R.id.cctvWeb_2);

        webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings = webView_2.getSettings();
        webSettings.setJavaScriptEnabled(true);

        webView_2.loadData("<html><head><style type='text/css'>body{margin:auto auto;text-align:center;} " +
                        "img{width:100%25;} div{overflow: hidden;} </style></head>" +
                        "<body><div><img src='http://192.168.197.72:8080/?action=stream'/></div></body></html>",
                "text/html", "UTF-8");
        /*webView_2.loadData("<html><head><style type='text/css'>body{margin:auto auto;text-align:center;} " +
                        "img{width:100%25;} div{overflow: hidden;} </style></head>" +
                        "<body><div><img src='http://192.168.178.72:7070'/></div></body></html>",
                "text/html", "UTF-8");*/
        webView.loadUrl("http://192.168.197.72:7070");
        // WebView 에 CCTV 화면 띄움
        /*webView.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                if (event.getAction() == MotionEvent.ACTION_DOWN) {
                    webView.reload();
                }
                return true;
            }
        }); // WebView 터치 시 새로고침*/
        webView_2.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                if (event.getAction() == MotionEvent.ACTION_DOWN) {
                    webView_2.reload();
                }
                return true;
            }});


        callText.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    AlertDialog.Builder builder = new AlertDialog.Builder(cctvActivity.this);
                    builder.setTitle("신고");
                    builder.setMessage("신고하시겠습니까?");
                    builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:112"));
                            startActivity(intent);
                        }
                    });
                    builder.setNegativeButton("No", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {

                        }
                    });
                    AlertDialog alertDialog = builder.create();
                    alertDialog.show();
                }
            }); // 신고하기 버튼 클릭 시 112 전화걸기로 이동
        }
    }

