# InvIndex
## Spark application to create the inverted index of a group of files
### Author: Luis Miguel Mejía Suárez (BalmungSan)
### Versión: 1.1.3 (23/05/2017)

Spark Application to compute the inverted index of a bunch of files in HDFS and saves the results in a mongo collection

The created index is of the form

    {word: "word", files: [{file: "file", count: "count"}]}

**Where:**

- **word:** is a word that appeared in the source files
in its _inflected_ form.
- **file:** is the filename of a document where the word appeared,
in the form _'/folder/file'_
- **count:** is the number of times the word appeared in that document

**Note:**
> the files array is sorted in decreasing order, where the comparison criterion is the number of times the word appeared in that document

### Usage
Compile

    $ sbt package

Run

    $ spark-submit --master yarn --deploy-mode cluster \
      --conf "spark.mongodb.output.uri=[mongo uri]" \
      --class "goofle.invindex.InvIndex" \
      target/scala-2.11/invindex_2.11-1.1.3.jar \
      [path]

**Where:**

- **mongo uri:** Is the URI to the mongo collection where the computed index will be saved _e.g. mongodb://localhost/db.collection_
- **path:** Is the route to the files to compute the inverted index _e.g. /datasets/gutenberg_

### Dependencies
These application depend on the [Mongo Spark Connector](https://github.com/mongodb/mongo-spark) and the [Mongo Scala Connector](https://docs.mongodb.com/spark-connector/master/scala-api/). Spark need to have access to these binaries.
Either these are installed in the cluster in a path where Spark can load them or are loaded from an online repository when the application starts execution.

- **Mongo Spark:** For load from an online repository add the following line to the run command. _before the application jar_.

	```--packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0```

- **Mongo Scala:** For load from an online repository add the following line to the run command. _before the application jar_.

	```--packages org.mongodb.scala:mongo-scala-driver_2.11:2.0.0```

### Notes
- Spanish and english [stop words](https://en.wikipedia.org/wiki/Stop_words) are ignored.
- **For the moment:** the _inflected_ form of a word means, all characters in lowercase and all diacritic vowel are mapped to its normal form. _e.g. Á => a_
	+ **Future work:** Compute and save the [word stem](https://en.wikipedia.org/wiki/Word_stem) of each word.
