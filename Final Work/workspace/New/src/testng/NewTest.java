package testng;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.AfterTest;
//import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.openqa.selenium.chrome.ChromeDriver;
public class NewTest {
	
	private WebDriver driver;
  @Test
  public void testEasy() {
	  driver.get("https://www.google.com/");
	  String title=driver.getTitle();
	  Assert.assertTrue(title.contains("Google")); 

  }
  @BeforeTest
  public void beforeTest() {
	  System.setProperty("webdriver.chrome.driver","C://Software//SEL_JAR-20210901T092836Z-001//SEL_JAR//chromedriver_win32//chromedriver.exe");
	  driver = new ChromeDriver();

  }

  @AfterTest
  public void afterTest() {
	  driver.quit();	

  }

}
