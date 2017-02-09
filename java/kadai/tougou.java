class tougou{
  public void fileRead(String filePath) {
      FileReader fr = null;
      BufferedReader br = null;
      try {
          fr = new FileReader(filePath);
          br = new BufferedReader(fr);

          String line;
          while ((line = br.readLine()) != null) {
              System.out.println(line);
          }
      } catch (FileNotFoundException e) {
          e.printStackTrace();
      } catch (IOException e) {
          e.printStackTrace();
      } finally {
          try {
              br.close();
              fr.close();
          } catch (IOException e) {
              e.printStackTrace();
          }
      }
  }
  public static void main(String args[]){
    String filename = "/home/tj/デスクトップ/data/uniprot.txt";
    fileread(filename);
  }
}
