name         := "InvIndex"
version      := "1.1.0"
organization := "goofle"

scalaVersion := "2.11.8"
scalacOptions in (Compile, doc) ++= Seq("-doc-title", "InvIndex")

libraryDependencies += "org.apache.spark"  %% "spark-sql" % "2.0.1"
libraryDependencies += "org.apache.spark"  %% "spark-core" % "2.0.1"
libraryDependencies += "org.mongodb.scala" %% "mongo-scala-driver" % "2.0.0"
libraryDependencies += "org.mongodb.spark" %% "mongo-spark-connector" % "2.0.0"
