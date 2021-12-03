package Mockito6.Mockito6;
import java.util.List; 
import java.util.ArrayList;  
public class ToDoBusiness {    
public ToDoService doService;    
public ToDoBusiness(ToDoService doService) {  
    this.doService = doService;  
}  
public void deleteTodosNotRelatedToHibernate(String user) {            
    List<String> Combinedlist = doService.getTodos(user);            
    for(String todos:Combinedlist) {  
        if(!todos.contains("Hibernate")) {  
            doService.deleteTodos(todos);  
        }  
    }  
}  
}  
