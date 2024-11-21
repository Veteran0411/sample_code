const a=[1,12,1,1,3,3,2]
let l=Array.from(new Set(a))
let s=[...l].sort((a,b)=>a-b)

console.log(l)
console.log(s)