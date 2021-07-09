import React, { useEffect, useState } from "react";
import { io } from "socket.io-client";
import Plot from 'react-plotly.js';

const App = () => {

	const [data, setData] = useState();
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		const socketURL = process.env.REACT_APP_SOCKET_URL;
		const socket = io(socketURL);
		socket.on("connect",()=>{
			socket.emit("ping_graph", {symbol: "ril.ns"});
		});
		socket.on("graph_plot", res => {
			if(loading===true){
				setLoading(false);
			}
			let response = JSON.parse(res);
			response.config = {responsive: true}
			setData(response);
		});
		return () => socket.disconnect();
	//eslint-disable-next-line
	}, []);

	return (
		<div className="wrapper">
			{loading?(
				<p>
					Loading...
				</p>
			):(
				<Plot
					{...data}
				/>
			)}
		</div>
	)
}

export default App