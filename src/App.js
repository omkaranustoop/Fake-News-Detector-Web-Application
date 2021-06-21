import React, { Component } from 'react'
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'


class App extends Component {
  constructor(props){
    super(props);
    this.state={input1:"Hello",score:"'Undefined-No Input'"};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event){
    console.log(event.target.name+' '+event.target.value);
    this.setState({[event.target.name]:event.target.value});
  }

  handleSubmit(event){
    event.preventDefault();
    this.setState({score:"'Processing Input'"})
    const url = "http://127.0.0.1:8000/result/";
    const bodyData = JSON.stringify({
       "input1":this.state.input1,
    });
    const output = {method:"POST",headers:{"Content-Type":"application/json"},body:bodyData};
    fetch(url,output)
    .then((resp) => resp.json())
    .then((respJ) => this.setState({score:respJ.score}))
  }

  render() {
    return (
      <div className="container-fluid my-5">
        <div className="row">
          <div className="col-sm-6 mx-auto text-green shadow-lg p-2">
            <h1 className="text-center">Spam Content Predictor</h1>
          </div>
        </div> 
        <div className="row">
              <div className="col-sm-3 mx-auto text-black shadow-lg p-2">
                <form onSubmit={this.handleSubmit}>
                <input type="text" name = "input1" placeholder="Submit your article here" onChange={this.handleChange} />
                <input type="submit" value="submit"></input> 
                </form> 
              </div>
            </div>
        <div className="row">
          <div className="col-sm-5 mx-auto text-black shadow-lg p-2">
            <h6><center>Spam Content Percentage in the article is {this.state.score}</center>
            </h6>
            </div>
            </div>
      </div>
    )
  }
}

export default App;
