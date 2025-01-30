#! /bin/bash

# Each function defines and launches a container
launch_node_01()    {
docker run -d \
	-p 9201:9200 -p 9601:9600 \
	-e "discovery.seed_hosts=os-node-01,os-node-02,os-node-03,os-node-04" \
	-e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
	-e "cluster.name=opensearch-dev-cluster" -e "node.name=os-node-01" \
	-e "cluster.initial_master_nodes=os-node-01,os-node-02,os-node-03,os-node-04" \
	-e "bootstrap.memory_lock=true" -e "path.repo=/mnt/snapshots" \
	--ulimit nofile=65536:65536 --ulimit memlock=-1:-1 \
	-v data-01:/usr/share/elasticsearch/data \
  	-v repo-01:/mnt/snapshots \
	--network opensearch-dev-net \
	--name os-node-01 \
	 docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
}

launch_node_02()    {
    docker run -d \
		-p 9202:9200 -p 9602:9600 \
		-e "discovery.seed_hosts=os-node-01,os-node-02,os-node-03,os-node-04" \
		-e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
		-e "cluster.name=opensearch-dev-cluster" -e "node.name=os-node-02" \
		-e "cluster.initial_master_nodes=os-node-01,os-node-02,os-node-03,os-node-04" \
		-e "bootstrap.memory_lock=true" -e "path.repo=/mnt/snapshots" \
		--ulimit nofile=65536:65536 --ulimit memlock=-1:-1 \
		-v data-02:/usr/share/elasticsearch/data \
	  	-v repo-01:/mnt/snapshots \
		--network opensearch-dev-net \
		--name os-node-02 \
		 docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
}
launch_node_03()    {
    docker run -d \
		-p 9203:9200 -p 9603:9600 \
		-e "discovery.seed_hosts=os-node-01,os-node-02,os-node-03,os-node-04" \
		-e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
		-e "cluster.name=opensearch-dev-cluster" -e "node.name=os-node-03" \
		-e "cluster.initial_master_nodes=os-node-01,os-node-02,os-node-03,os-node-04" \
		-e "bootstrap.memory_lock=true" -e "path.repo=/mnt/snapshots" \
		--ulimit nofile=65536:65536 --ulimit memlock=-1:-1 \
		-v data-03:/usr/share/elasticsearch/data \
	  	-v repo-01:/mnt/snapshots \
		--network opensearch-dev-net \
		--name os-node-03 \
		 docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
}

launch_node_04()    {
	docker run -d \
		-p 9204:9200 -p 9604:9600 \
		-e "discovery.seed_hosts=os-node-01,os-node-02,os-node-03,os-node-04" \
		-e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
		-e "cluster.name=opensearch-dev-cluster" -e "node.name=os-node-04" \
		-e "cluster.initial_master_nodes=os-node-01,os-node-02,os-node-03,os-node-04" \
		-e "bootstrap.memory_lock=true" -e "path.repo=/mnt/snapshots" \
		--ulimit nofile=65536:65536 --ulimit memlock=-1:-1 \
		-v data-04:/usr/share/elasticsearch/data \
	  	-v repo-01:/mnt/snapshots \
		--network opensearch-dev-net \
		--name os-node-04 \
		 docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
}
launch_node_dashboards()	{
	docker run -d \
		-p 5601:5601 --expose 5601 \
		-e "DISABLE_SECURITY_DASHBOARDS_PLUGIN=true" \
		-e 'OPENSEARCH_HOSTS=["http://node-01:9200","http://node-02:9200"]' \
		--network opensearch-dev-net \
		--name os-dashboards-01 \
		opensearchproject/opensearch-dashboards:1.3.7
}

launch_node_01
launch_node_02
launch_node_03
launch_node_04
# launch_node_dashboards