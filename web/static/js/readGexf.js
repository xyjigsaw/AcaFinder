var dom = document.getElementById("homeRelation");
var myChart = echarts.init(dom);
            var app = {};
            option = null;
            myChart.showLoading();
            $.get('../static/data/les-miserables.gexf', function (xml) {
                myChart.hideLoading();

                var graph = echarts.dataTool.gexf.parse(xml);
                var categories = [];
                for (var i = 0; i < 9; i++) {
                    categories[i] = {
                        name: '类目' + i
                    };
                }
                graph.nodes.forEach(function (node) {
                    node.itemStyle = null;
                    node.value = node.symbolSize;
                    node.symbolSize /= 1.5;
                    node.label = {
                        show: node.symbolSize > 30
                    };
                    node.category = node.attributes.modularity_class;
                });
                option = {
                    title: {},
                    tooltip: {},
                    legend: [{
                        // selectedMode: 'single',
                        data: categories.map(function (a) {
                            return a.name;
                        })
                    }],
                    animationDuration: 10000,
                    animationEasingUpdate: 'quinticInOut',
                    series : [
                        {
                            name: 'Academia Network',
                            type: 'graph',
                            layout: 'none',
                            data: graph.nodes,
                            links: graph.links,
                            categories: categories,
                            roam: true,
                            zoom: 2.0,
                            focusNodeAdjacency: true,
                            itemStyle: {
                                borderColor: '#fff',
                                borderWidth: 1,
                                shadowBlur: 10,
                                shadowColor: 'rgba(0, 0, 0, 0.3)'
                            },
                            label: {
                                position: 'right',
                                formatter: '{b}'
                            },
                            lineStyle: {
                                color: 'source',
                                curveness: 0.3
                            },
                            emphasis: {
                                lineStyle: {
                                    width: 10
                                }
                            }
                        }
                    ]
                };

                myChart.setOption(option);
            }, 'xml');
            if (option && typeof option === "object") {
                myChart.setOption(option, true);
            }