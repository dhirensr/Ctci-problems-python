class Vector {
    constructor(x,y) {
        this.x=x;
        this.y=y;
    }
    plus(vector_object){
        return [this.x+vector_object.x,this.y+vector_object.y];
    }

    minus(vector_object){
        return [this.x-vector_object.x,this.y-vector_object.y];
    }
}

class Group {
    constructor(members=[]){
        this.members=members;
    }
    add(number){
        if(!this.members.includes(number)){
            this.members.push(number);
            return this.members;
        }
    }
    delete(number){
        if(this.members.includes(number)){
            this.members.pop();
            return this.members;
        }
    }
    has(number){
        if(this.members.includes(number)){
            return true;
        }
        else{
            return false;
        }
    }


    [Symbol.iterator]() {
        return new GroupIterator(this);
    }
}

class GroupIterator{
    constructor(members){
        this.counter=-1;
        this.members=members.members;
    }
    next() {
        this.counter++;
        if(this.counter==this.members.length){
            return {done : true};
        }
        else {
            return {value: this.members[this.counter],done: false};
        }
    }
}
