import React from "react";

class TodoForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = {text: '', users: []}
    }

    handleChange(event){
        this.setState(
            {
            [event.target.name] : event.target.value
            }
        );
    }

    handleUserChange(event){
        if(!event.target.selectedOptions) {
        this.setState({
            'users':[]
            })
            return;
        }
        let users = []
        for(let i = 0; i < event.target.selectedOptions.length; i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState(
            {'users':users}
        )
    }

    handleSubmit(event){
        this.props.create_todo(this.state.text, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="text"></label>
                    <input type="text" name="text" placeholder="text"
                        value={this.state.text}
                        onChange={(event)=>this.handleChange(event)} />
                  </div>
                  <select name="users" multiple onChange={(event) => this.handleUserChange(event)}>
                    {this.props.todos.map((item)=> <option value={item.id}>{item.first_name}</option>)}
                  </select>

                <input type="submit" value="Save" />
            </form>
            )
    }

}
export default TodoForm
