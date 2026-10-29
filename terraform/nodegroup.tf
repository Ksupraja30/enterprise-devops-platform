resource "aws_eks_node_group" "node_group" {
  cluster_name = aws_eks_cluster.eks.name
  node_group_name = "monitoring-nodes"
  node_role_arn = aws_iam_role.eks_node_role.arn

  subnet_ids = [
    aws_subnet.public_1.id,
    aws_subnet.public_2.id
  ]

  scaling_config {
    desired_size = 2
    min_size = 1
    max_size = 4
  }
  instance_types = ["t3.medium"]
}