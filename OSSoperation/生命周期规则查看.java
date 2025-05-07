import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.model.LifecycleRule;
import java.util.List;

        try {
            // bucketName 定义
            String bucketName = "xtzhdd";
            // 获取生命周期规则。
            List<LifecycleRule> rules = ossClient.getBucketLifecycle(bucketName);

            // 查看生命周期规则。
            for (LifecycleRule rule1 : rules) {
                // 查看规则ID。
                System.out.println("rule id: " + rule1.getId());

                // 查看规则前缀。
                System.out.println("rule prefix: " + rule1.getPrefix());

                // 查看规则标签。
                if (rule1.hasTags()) {
                    System.out.println("rule tagging: "+ rule1.getTags().toString());
                }

                //查看过期天数规则。
                if (rule1.hasExpirationDays()) {
                    System.out.println("rule expiration days: " + rule1.getExpirationDays());
                }

                //查看过期日期规则。
                if (rule1.hasCreatedBeforeDate()) {
                    System.out.println("rule expiration create before days: " + rule1.getCreatedBeforeDate());
                }

                //查看过期分片规则。
                if(rule1.hasAbortMultipartUpload()) {
                    if(rule1.getAbortMultipartUpload().hasExpirationDays()) {
                        System.out.println("rule abort uppart days: " + rule1.getAbortMultipartUpload().getExpirationDays());
                    }

                    if (rule1.getAbortMultipartUpload().hasCreatedBeforeDate()) {
                        System.out.println("rule abort uppart create before date: " + rule1.getAbortMultipartUpload().getCreatedBeforeDate());
                    }
                }
            }

        }
