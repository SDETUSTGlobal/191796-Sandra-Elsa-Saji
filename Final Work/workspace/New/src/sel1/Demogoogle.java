package sel1;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Demogoogle {
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver","C://Software//SEL_JAR-20210901T092836Z-001//SEL_JAR//chromedriver_win32//chromedriver.exe");
		WebDriver driver= new ChromeDriver();
		driver.manage().window().maximize();
		driver.navigate().to("https://www.amazon.in/");
		driver.findElement(By.id("nav-orders")).getText();
		driver.findElement(By.id("twotabsearchtextbox")).sendKeys("IPhone");
		driver.findElement(By.id("nav-search-submit-text")).click();
		driver.findElement(By.id("ntwotabsearchtextbox")).clear();
		driver.navigate().back();
		driver.close();
	}
}
//C://Software//SEL_JAR-20210901T092836Z-001//SEL_JAR//chromedriver_win32//chromedriver.exe