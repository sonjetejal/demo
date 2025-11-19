<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>MyApp</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>MyApp</name>
  <url>http://maven.apache.org</url>
 
  <properties>
  <maven.compiler.source>8</maven.compiler.source>
  <maven.compiler.target>8</maven.compiler.target>
  </properties>
 
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
   <plugins>
    <plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <version>3.0.0</version>
    <executions>
    <execution>
    <goals>
     <goal>java</goal>
   </goals>
   </execution>
   </executions>
   <configuration>
   <mainClass>com.example.App</mainClass>
   </configuration>
   </plugin>
  </plugins>
  </build>
</project>




touch index.html
touch dockerfile
sudo docker build -t folder name .
sudo docker run -p 8081:80 -d folder name

docker file madhye type kharych
FROM httpd:2.4
COPY index.html /usr/local/apache2/htdocs/

index.html madhye html code type kharych

go to browser and type localhost:8081
        

    


