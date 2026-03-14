function initMinimap(){

const miniContainer = document.getElementById("minimap")

const miniNodes = new vis.DataSet(GRAPH_DATA.nodes)
const miniEdges = new vis.DataSet(GRAPH_DATA.edges)

const miniNetwork = new vis.Network(
miniContainer,
{nodes:miniNodes,edges:miniEdges},
{
physics:false,
interaction:false
}
)

AppState.minimap = miniNetwork

/* navigation */

miniContainer.addEventListener("mousemove",function(e){

const rect = miniContainer.getBoundingClientRect()

const x = (e.clientX-rect.left)/rect.width
const y = (e.clientY-rect.top)/rect.height

AppState.graph.moveTo({

position:{
x:(x-0.5)*4500,
y:(y-0.5)*4500
},

animation:false

})

})

}