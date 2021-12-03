package testng;

import org.testng.annotations.Test;

public class Test2 {
  @Test(enabled=false)
  public void test3() {
	  System.out.println("test3");
  }
  
  @Test
  public void test4() {
	  System.out.println("test4");
  }
}
