import React from "react";


export class TablesPage extends React.Component{
    constructor(props){
        super(props);
        this.tablesProvider = props.tablesProvider()
    }

    render(){
        return (
            <div>
                <img src="XXL.jpeg" alt="(("/>
                {this.bookForm()}
            </div>
        )
    }

    bookForm(){
        return (
            <div>
                <form className="anForm" name="bookForm" onSubmit={this.sendRequest}>
                    <select className="form-select" id="item" aria-label="Default select example">
                        <option value="61">Зона переговоров 1</option>
                        <option value="62">Зона переговоров 2</option>
                        <option value="1" selected>Рабочее место 1</option>
                        <option value="2">Рабочее место 2</option>
                        <option value="3">Рабочее место 3</option>
                        <option value="4">Рабочее место 4</option>
                        <option value="5">Рабочее место 5</option>
                        <option value="6">Рабочее место 6</option>
                        <option value="7">Рабочее место 7</option>
                        <option value="8">Рабочее место 8</option>
                        <option value="9">Рабочее место 9</option>
                        <option value="10">Рабочее место 10</option>
                        <option value="11">Рабочее место 11</option>
                        <option value="12">Рабочее место 12</option>
                        <option value="13">Рабочее место 13</option>
                        <option value="14">Рабочее место 14</option>
                        <option value="15">Рабочее место 15</option>
                        <option value="16">Рабочее место 16</option>
                        <option value="17">Рабочее место 17</option>
                        <option value="18">Рабочее место 18</option>
                        <option value="19">Рабочее место 19</option>
                        <option value="20">Рабочее место 20</option>
                        <option value="21">Рабочее место 21</option>
                        <option value="22">Рабочее место 22</option>
                        <option value="23">Рабочее место 23</option>
                        <option value="24">Рабочее место 24</option>
                        <option value="25">Рабочее место 25</option>
                        <option value="26">Рабочее место 26</option>
                        <option value="27">Рабочее место 27</option>
                        <option value="28">Рабочее место 28</option>
                        <option value="29">Рабочее место 29</option>
                        <option value="30">Рабочее место 30</option>
                        <option value="31">Рабочее место 31</option>
                        <option value="32">Рабочее место 32</option>
                        <option value="33">Рабочее место 33</option>
                        <option value="34">Рабочее место 34</option>
                        <option value="35">Рабочее место 35</option>
                        <option value="36">Рабочее место 36</option>
                        <option value="37">Рабочее место 37</option>
                        <option value="38">Рабочее место 38</option>
                        <option value="39">Рабочее место 39</option>
                        <option value="40">Рабочее место 40</option>
                        <option value="41">Рабочее место 41</option>
                        <option value="42">Рабочее место 42</option>
                        <option value="43">Рабочее место 43</option>
                        <option value="44">Рабочее место 44</option>
                        <option value="45">Рабочее место 45</option>
                        <option value="46">Рабочее место 46</option>
                        <option value="47">Рабочее место 47</option>
                        <option value="48">Рабочее место 48</option>
                        <option value="49">Рабочее место 49</option>
                        <option value="50">Рабочее место 50</option>
                        <option value="51">Рабочее место 51</option>
                        <option value="52">Рабочее место 52</option>
                        <option value="53">Рабочее место 53</option>
                        <option value="54">Рабочее место 54</option>
                        <option value="55">Рабочее место 55</option>
                        <option value="56">Рабочее место 56</option>
                        <option value="57">Рабочее место 57</option>
                        <option value="58">Рабочее место 58</option>
                        <option value="59">Рабочее место 59</option>
                        <option value="60">Рабочее место 60</option>
                    </select>
                    <input type="date" id="date" name="date"/>
                    <br/>
                    <div className="container-login100-form-btn">
                        <button type="submit" className="login100-form-btn">Отправить</button>
                    </div>
                </form>
                <span id="result"/>
            </div>

        )
    }

    contentUpdate(content){
        this.setState({current: content})
    }

    sendRequest = (event) => {
        event.preventDefault();
        document.getElementById("result").innerText = (this.tablesProvider.sendForm(this.getFormData()))
            ? "Удачно забронировано"
            : "Увы, но слот уже занят на это время"
    }

    getFormData(){
        const data = {
            item: document.getElementById("item").value,
            date: document.getElementById("date").value
        }
        document.forms.bookForm.reset()
        return data
    }
}