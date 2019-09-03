export class Task {
    constructor(public id: number,
                public name: string,
                public status: string,
                public date_start: Date,
                public date_end: Date) {
    }
}