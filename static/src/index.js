import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootstrap/dist/js/bootstrap.min.js";
import {register_container} from "./js/container";

import ReactDOM from "react-dom";
import React from "react";


const container = register_container()
console.log('here')
let app = container.resolve('app')
console.log(app)
ReactDOM.render(<app.Render/>, document.getElementById('root'))