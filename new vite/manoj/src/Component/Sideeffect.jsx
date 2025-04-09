import React from 'react'

const sideEffect = () => {

    useEffect(() => {
        first

        return () => {
            second
        }
    }, [third])

    return (
        <div>sideEffect</div>
    )
}

export defaults sideEffect