import { Component, OnInit } from '@angular/core';
import { TaskService } from 'src/services/task-service.service';
import { Task } from 'src/model/task';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {

  public tasks: Array<Task>;

  constructor(private _taskService: TaskService) { }

  ngOnInit() {
    this._taskService.getTasks().subscribe(
      data => {
        this.tasks = data.data 
      },
      error => {
        console.log(error)
      });
  }


  editTaskClickEvent(event: Event, id: number) : void {
    console.log("Event edit task clicked", id);
  }

  
  deleteTaskClickEvent(event: Event, id: number) : void {
    this._taskService.deleteTask(id).subscribe(
      data => {
        console.log(data)
      }, 
      error => {
        console.log(error)
      });
  }

  

}
