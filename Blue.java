public class Blue{
    public static void main(String[] args){
        Player1 player1 = new Player1();

        String name = player1.name;
        String weapon = player1.weapon;

        System.out.println(name);
        System.out.println("action" + weapon);
    }
}

class Player1{
    public String name = "yoichi";
    public String weapon = "vision";
    public String callPlayer(){
        return "Call";
    }
}

class Player2{
    public String name = "meguru";
}

class callPlayer{
    
}