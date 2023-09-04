import React from 'react';

const TodoItem = ({todo,delete_todo}) => {
    return (
        <tr>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.updated}
            </td>
            <td>
                <button onClick={()=>delete_todo(todo.user)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const TodoList = ({todos,delete_todo}) => {
    return (
        <table>
            <th>
                text
            </th>
            <th>
                User
            </th>
            <th>
                Updated
            </th>
            <th>

            </th>
            {todos.map((todo) => <TodoItem todo={todo} delete_todo={delete_todo}/>)}
        </table>
    )
}

export default TodoList;
