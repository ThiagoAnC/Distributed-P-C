import processing.sound.*;
import processing.video.*;

AudioIn voice;
Reverb reverb;
SoundFile soundfile;
PImage bg;
Capture cam;

void setup() {
  
  bg = loadImage("Bottom.jpg");
  String[] cameras = Capture.list();  
  size(300,200);
        
  // Declara a entrada de voz
  voice = new AudioIn(this, 0);
  
  //Declara o arquivo de áudio
  soundfile = new SoundFile(this, "Sea Sounds.mp3");

  // Reproduz o áudio acima num looping
  soundfile.loop();
    
  // Cria o efeito de reverberação
  reverb = new Reverb(this);

  // Reproduz a voz que foi dada como entrada
  voice.play();

  // Aplica os efeitos na voz de entrada
  reverb.process(voice);
  reverb.wet(1);
  
  //Inicializa a camera
  //cam = new Capture(this, cameras[0]);
  //cam.start();
  
}      

void draw() {
    background(bg);
    
    //if (cam.available() == true) {
    //   cam.read();
    //}
    //tint(255,64);
    //image(cam, 0, 0);
    
}
