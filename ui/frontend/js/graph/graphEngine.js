function initGraph(){

const nodes = new vis.DataSet(GRAPH_DATA.nodes)
const edges = new vis.DataSet(GRAPH_DATA.edges)

AppState.nodes = nodes
AppState.edges = edges

const container = document.getElementById("graphCanvas")

const network = new vis.Network(
container,
{nodes:nodes,edges:edges},
{

nodes:{
borderWidth:2,

color:{
background:"#0f172a",
border:"#60a5fa"
},

font:{
color:"#e5e7eb",
face:"monospace"
}
},

layout:{
improvedLayout:true
},

physics:{
enabled:false,
barnesHut:{
gravitationalConstant:-9000,
springLength:200
}
},

interaction:{
dragView:false,
zoomView:false
}

}
)

AppState.graph = network

/* enable physics when user clicks */

network.on("click",function(){

network.setOptions({
physics:{enabled:true}
})

})

}