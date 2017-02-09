import java.io.*;

class q2{
  public static void main(String[] args){
      int i = 0;
      String filename = "/home/tj/デスクトップ/data/tougou.txt";
      try (BufferedReader in = new BufferedReader(new FileReader(new File(filename)))){
          String line;
          while((line = in.readLine()) != null){
            String seq = line.split("\t")[8];
            String sites = line.split("\t")[9];
            for(String site: sites.split(",")){
              int pos = Integer.parseInt(site);
              String res = seq.substring(pos-1,pos);
              System.out.println(seq.substring(pos-1,pos));
            }
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
