interface MainProps{
    name: string;
    age: number;
}

function hello(person:MainProps){
    return `${person.name} and their age is ${person.age}`
}
const kyle ={name: 'kyle', age: 25}
console.log(kyle)