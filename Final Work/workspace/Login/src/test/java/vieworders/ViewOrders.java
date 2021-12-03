package vieworders;
import org.openqa.selenium.By;   
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.chrome.ChromeDriver;  
import cucumber.annotation.en.Given;   
import cucumber.annotation.en.Then;   
import cucumber.annotation.en.When; 
public class ViewOrders {
	WebDriver driver= null;
	   @Given("^I am on view all orders page$")   
	   public void goToViewOrders() {   
		   driver= new ChromeDriver();
		   driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/default.aspx");   
	   }   
	      
	   @When("^I click on check all button$")   
	   @Then("^All orders are checked$")
	   public void Checkall(){   
		  driver.findElement(By.id("ctl00_MainContent_btnCheckAll")).click();//check all  
		 }   
	   @When("^I click on uncheck all button$")   
	   @Then("^All orders are unchecked$")
	   public void Uncheckall(){    
		  driver.findElement(By.id("ctl00_MainContent_btnCheckAll")).click();//uncheck all
	   }  
	   @When("^I click on desired orders check box$")   
	   @Then("^desired orders checked/unchecked$")
	   public void Boxcheck(){ 
		   driver.findElement(By.id("ctl00_MainContent_orderGrid_ctl02_OrderSelectorl")).click();//click on pauls order to check
		   driver.findElement(By.id("ctl00_MainContent_orderGrid_ctl02_OrderSelector")).click();//click on pauls order to uncheck

	   }  
	   @When("^I click on delete button$")   
	   @Then("^Selected orders are deleted$")
	   public void DeleteAll(){ 
		   driver.findElement(By.id("ctl00_MainContent_orderGrid_ctl03_OrderSelector")).click();
			  driver.findElement(By.id("ctl00_MainContent_orderGrid_ctl04_OrderSelector")).click();
			  driver.findElement(By.id("ctl00_MainContent_btnDelete")).click();//delete selected
	   }  
	      
	   @When("^I click on edit button$")   
	   @Then("^navigate to edit page$")
	   public void Edit(){ 
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/div[3]/table/tbody/tr[2]/td[13]/input")).click();//edit selected
	  
	    driver.close();  
	   }
}
