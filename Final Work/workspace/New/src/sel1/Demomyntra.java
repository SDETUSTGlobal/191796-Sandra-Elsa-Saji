package sel1;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Demomyntra {

	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver","C://Software//SEL_JAR-20210901T092836Z-001//SEL_JAR//chromedriver_win32//chromedriver.exe");
		WebDriver driver= new ChromeDriver();
		driver.manage().window().maximize();
		driver.navigate().to("https://www.myntra.com/");
		driver.findElement(By.xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/input")).sendKeys("ALDO");
		driver.findElement(By.id("/html/body/div[1]/div/div/header/div[2]/div[3]/a/span")).click();
		driver.close();

	}

}
