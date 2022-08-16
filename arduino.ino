#include <Servo.h>
String str="";
int is_start = 0;
// khai báo các chân tín hiệu của Arduino
#define enableDongco 3  
#define servoDoto 4
#define servoDonho 5
#define servoXanhto 6
#define servoXanhnho 7
#define sensorXanhnho 8
#define sensorXanhto 9
#define sensorDonho 10
#define sensorDoto 11
#define sensorHong 12
#define in1Dongco A0
#define in2Dongco A1

Servo svDoto;
Servo svDonho;
Servo svXanhto;
Servo svXanhnho;

void dungDongCo() {
  digitalWrite(in1Dongco, 0); // cái in1 và in2 là các chân của động cơ  
  digitalWrite(in2Dongco, 0);
            

}
void chayDongCo() {
  analogWrite(enableDongco, 255);
  digitalWrite(in1Dongco, 1); // số 1 ở chỗ in1Dongco đây có nghĩa là động cơ nó sẽ chạy đúng chiều 
  digitalWrite(in2Dongco, 0);

}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
   pinMode(servoDoto, OUTPUT); // PinMode có 2 cái INPUT và OUTPUT tức là để đưa tín hiệu input ra output 
  pinMode(servoDonho, OUTPUT); // servoDoto ở đây là cảm biến tiệm cận của đỏ to
  pinMode(servoXanhto, OUTPUT);
  pinMode(servoXanhnho, OUTPUT); //PinMode là dùng để thiết đặt pin là một output, có nghĩa là làm cho pin ý có một trở kháng (cho dòng điện đi ra),điều này có nghĩa là pin sẽ cung cấp một lượng điện đáng kể cho các mạch khác  
  
  pinMode(in1Dongco, OUTPUT); // PinMode định cấu hình chân được chỉ định để hoạt động như một đầu vào hoặc một đầu ra, có cú pháp là pinMOde(pin, mode)
  pinMode(in2Dongco, OUTPUT);
  pinMode(enableDongco, OUTPUT);
  
  pinMode(sensorXanhnho, INPUT);
  pinMode(sensorXanhto, INPUT);
  pinMode(sensorDonho, INPUT);
  pinMode(sensorDoto, INPUT);
  
  pinMode(sensorHong,INPUT); // servoHong là servo được dùng đầu tiên để phát hiện có táo
  
  svDoto.attach(servoDoto); //svDOto là động servo để gạt quả táo (dùng attach ở đây là để kết nối tín hiệu từ cảm biến tiệm cận sang động cơ servo để gạt)
  svDonho.attach(servoDonho);
  svXanhto.attach(servoXanhto);
  svXanhnho.attach(servoXanhnho);
  svDoto.write(0);
  svDonho.write(0);
  svXanhto.write(0);
  svXanhnho.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available()>0){
    str=Serial.readStringUntil('\n');
    // an nut khoi dong
    if(str=="stop"){ // nếu bằng 0 thì sẽ dừng động cơ 
      dungDongCo();
    }else if (str == "start") { // nếu bằng 1 thì sẽ chạy động cơ
      chayDongCo();
    }else if (str == "reset"){
      dungDongCo();
      is_start=0;
    }
  }
  if (digitalRead(sensorHong) == 0 && is_start == 0) {
    Serial.println("1");
    delay(400);
    dungDongCo();
    is_start = -1;
  }
  // chay dong co sau khi phan loai
  if (str == "taodoto"){
    chayDongCo();
  }
  if (str == "taodonho"){
    chayDongCo();
  }
  if (str == "taoxanhto"){
    chayDongCo();
  }
  if (str == "taoxanhnho"){
    chayDongCo();
  }
  if (str == "taoHong"){
    chayDongCo();
  }
  if (str == "taodoto" && digitalRead(sensorDoto) == 0 && is_start==-1) {//Cảm biến phát hiện có vật và python gửi tín hiệu về là "taodoto" thì dừng động cơ để gạt táo
    dungDongCo();
    delay(500);// Sau khi cảm biến nhận tín hiệu đc sau 0,5s thì nó sẽ gạt động cơ
    svDoto.write(90); // ở đây là động cơ quay 90 độ 
    delay(1000);// sau khi quay xong 90 độ thì nó sẽ dừng lại 1s và quay lại ban đầu 
    svDoto.write(0);// ở đây là quay lại vị trí góc như ban đầu 0 độ
    str = -1;
    is_start = 0;
    Serial.println("2");//Arduino gửi tín hiệu lên báo cho Python biết là đã thực hiện xong hành động gạt
  }
  if (str == "taodonho" && digitalRead(sensorDonho) == 0&& is_start==-1) {//Cảm biến phát hiện có vật và python gửi tín hiệu về là "taodonho" thì dừng động cơ để gạt táo
    dungDongCo();
    delay(500);
    svDonho.write(90);
    delay(1000);
    svDonho.write(0);
    str = -1;
    is_start=0;
    Serial.println("2");
  }
  if (str == "taoxanhnho" && digitalRead(sensorXanhnho) == 0&& is_start==-1) { //Cảm biến phát hiện có vật và python gửi tín hiệu về là "taodoxanhnho" thì dừng động cơ để gạt táo
    dungDongCo();
    delay(500);
    svXanhnho.write(90);
    delay(1000);
    svXanhnho.write(0);
    str = -1;
    is_start=0;
    Serial.println("2");
  }
  if (str == "taoxanhto" && digitalRead(sensorXanhto) == 0&& is_start==-1) {//Cảm biến phát hiện có vật và python gửi tín hiệu về là "taodoxanhto" thì dừng động cơ để gạt táo
    dungDongCo();
    delay(500);
    svXanhto.write(90);
    delay(1000);
    svXanhto.write(0);
    str = -1;
    is_start=0;
    Serial.println("2");
  }
  delay(500);
}