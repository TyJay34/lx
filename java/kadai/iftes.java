import java.io.*;

class iftes{
  public static void main(String[] args){
      int i = 0;
      String filename = "/home/tj/デスクトップ/data/uniprot.txt";
      try (BufferedReader in = new BufferedReader(new FileReader(new File(filename)))){
          String line;
          while((line = in.readLine()) != null){
            if(i != 0){
              String name = line.split("\t")[1];
              if( name.split("_")[1] == "HUMAN" ){
                System.out.println(name);
              }
            }
            i++;
          }
      } catch (FileNotFoundException e){
          e.printStackTrace();
          System.exit(-1); // 0 以外は異常終了
      } catch (IOException e){
          e.printStackTrace();
          System.exit(-1);
      }
  }
}
