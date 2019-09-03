import { Task } from './task';

export class ApiResponse {
    constructor(public message: String, public data: Array<Task>){}
}