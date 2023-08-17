import React from 'react';

const TodoItem = ({todo}) => {
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
        </tr>
    )
}

const TodoList = ({todos}) => {
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
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList;
