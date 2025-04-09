import React, { useState} from 'react'

const Counter = () => {
const [count,setCount]= useState(0);

function handleclick() {
    setCount(count + 1)
    
    console.log(count)
}
 return (
    <div>
        <h3>count: {count}</h3>
        <button onClick={handleclick}>ADD</button>
    </div>
 )
}

export default Counter