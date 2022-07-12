
(cl:in-package :asdf)

(defsystem "test_msg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "TEST" :depends-on ("_package_TEST"))
    (:file "_package_TEST" :depends-on ("_package"))
  ))