import java.io.*;

class aaa{
  public static void main(String[] args){
    File outfile = new File("/home/tj/デスクトップ/data/tougou.txt");
    try(PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(outfile)))){
      int i = 0;
      String filename = "/home/tj/デスクトップ/data/uniprot.txt";
      try (BufferedReader in = new BufferedReader(new FileReader(new File(filename)))){
          String line;
          while((line = in.readLine()) != null){
            if(i != 0){
              String name = line.split("\t")[1];
              //System.out.println(name);
              if(name.split("_")[1].equals("HUMAN")){
                String sites = "";
                try(BufferedReader in2 = new BufferedReader(new FileReader(new File("/home/tj/デスクトップ/data/ogtsite.txt")))){
                  String ogtsite;
                  while((ogtsite = in2.readLine()) != null){
                    //System.out.println(ogtsite.split("\t")[0] + "\t" + name);
                    if(ogtsite.split("\t")[0].equals(name)){
                      sites = sites + ogtsite.split("\t")[1] + ",";
                    }
                    //break;
                  }
                  //break;
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                    System.exit(-1); // 0 以外は異常終了
                } catch (IOException e){
                    e.printStackTrace();
                    System.exit(-1);
                }
                System.out.println(line + "\t" + sites);
                pw.println(line + "\t" + sites);
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
    }catch (IOException e){
        e.printStackTrace();
        System.exit(-1);
    }
  }
}
