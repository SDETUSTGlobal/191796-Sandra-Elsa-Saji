package Orders;
import org.openqa.selenium.By;   
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.chrome.ChromeDriver;  
import cucumber.annotation.en.Given;   
import cucumber.annotation.en.Then;   
import cucumber.annotation.en.When; 
import cucumber.annotation.en.And; 
public class OrdersPage {
	WebDriver driver= null;
	   @Given("^I am on orders page$")   
	   public void goToViewOrders() {   
		   driver= new ChromeDriver();
		   driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Process.aspx");   
	   }   
	      
	   @When("^I chooses the type of product required $")   
	   @Then("^he unit price of the product is displayed in the corresponding textbox$")
	   public void Product(){   
		  driver.findElement(By.id("ctl00_MainContent_fmwOrder_ddlProduct")).click(); 
		  driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtQuantity")).sendKeys("2");
		 } 
	   @And("^I click the calculate button $")   
	   @Then("^the total cost is displayed in the corresponding textbox $")
	   public void Calculate(){    
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();
	   }  
	   public void Address(){   
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtName")).sendKeys("Sandra Elsa Saji");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("Karipuzha");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("Alapuzha");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("Kerala");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("690511");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_0")).click();
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("1234567890");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("09/22");
			 } 
		   @When("^I click the Process button $")   
		   @Then("^the payment is processed $")
		   public void Process(){    
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_InsertButton")).click();
		   } 
	   @When("^I click on the reset button$")   
	   @Then("^all the data from the columns are erased $")
	   public void Reset(){ 
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input")).click();
			  driver.close(); 
	   }  
	      

}
