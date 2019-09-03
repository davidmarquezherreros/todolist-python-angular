import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Task } from 'src/model/task';
import { Configuration } from 'src/model/configuration';
import { Observable } from 'rxjs';
import { ApiResponse } from 'src/model/ApiResponse';

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  private task: Task;
  private apiUrl: string;
  private static method: string = "tasks";

  constructor(private httpClient: HttpClient) { 
    this.apiUrl = Configuration.apiUrl + Configuration.urlDelimeter+ TaskService.method;
  }


  getTask(id: number): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(this.apiUrl + Configuration.urlDelimeter + id);
  }

  getTasks(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(this.apiUrl);
  }

  deleteTask(id: number): Observable<ApiResponse> {
    return this.httpClient.delete<ApiResponse>(this.apiUrl + Configuration.urlDelimeter + id);
  }

  updateTask(task: Task): Observable<ApiResponse> {
    return this.httpClient.put<ApiResponse>(this.apiUrl + Configuration.urlDelimeter + task.id, task);
  }

  createTask(task: Task): Observable<ApiResponse> {
    return this.httpClient.post<ApiResponse>(this.apiUrl + Configuration.urlDelimeter + task.id, task);
  }

}
