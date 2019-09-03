import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TaskService } from 'src/services/task-service.service';
import { Task } from 'src/model/task';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-task-detail',
  templateUrl: './task-detail.component.html',
  styleUrls: ['./task-detail.component.css']
})
export class TaskDetailComponent implements OnInit {

  private _idTask: number = null;
  private static paramName: string = 'id'


  public taskDetails: Task;
  public taskForm: FormGroup;


  constructor(
      private _route: ActivatedRoute,
      private _taskService: TaskService,
      private _formBuilder: FormBuilder
      ) { 
        this.taskForm = this._formBuilder.group(
          {
            name: '',
            status: '',
            date_start: '',
            date_end: ''
          }
        )
  }

  ngOnInit() {
    this._route.params.subscribe(
      (data) => {
        this._idTask = data[TaskDetailComponent.paramName]
        if(this._idTask != undefined) this.retrieveTaskDetails()
      });
  }

  retrieveTaskDetails(): void {
    this._taskService.getTask(this._idTask).subscribe(
      (data) => {
        this.taskDetails = data.data[0]
        this.populateTaskForm()
      },
      (error) => {
        console.log(error)
      }
    )
  }

  populateTaskForm(): void {
    this.taskForm = this._formBuilder.group(
      {
        name: this.taskDetails.name,
        status: this.taskDetails.status,
        date_start: this.taskDetails.date_start,
        date_end: this.taskDetails.date_end
      }
    )
  }

  onSubmit(value: any) {
    console.log(value)
  }

}
