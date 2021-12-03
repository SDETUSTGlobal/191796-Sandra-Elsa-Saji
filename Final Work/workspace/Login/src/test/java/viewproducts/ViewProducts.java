package viewproducts;
import org.openqa.selenium.By;   
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.chrome.ChromeDriver;  
import cucumber.annotation.en.Given;   
import cucumber.annotation.en.Then;   
import cucumber.annotation.en.When; 

public class ViewProducts {
	WebDriver driver= null;
	   @Given("^I am on view all orders page$") 
	   public void goToViewOrders() {   
		   driver= new ChromeDriver();
		   driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Default.aspx");   
	   } 
	   @When("^I click on view all products$")
	   @Then("^I see List of Products$")
	   public void goToViewProducts(){ 
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[1]/ul/li[2]/a")).click();//view all products
	  
	    driver.close();  
	   }
	   
}
