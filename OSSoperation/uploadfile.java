import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.model.Bucket;
import java.io.ByteArrayInputStream;
import java.util.List;


            String objectName = "exampledir/exampleobject.txt";
            String content = "Hello OSS";
            String bucketName = "xtzhdd";
            ossClient.putObject(bucketName, objectName, new ByteArrayInputStream(content.getBytes()));
            System.out.println("2. 文件 " + objectName + " 上传成功。");
