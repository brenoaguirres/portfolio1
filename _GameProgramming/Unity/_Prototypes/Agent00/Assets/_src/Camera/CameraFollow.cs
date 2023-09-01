using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    [SerializeField]
    private Transform playerTransform;
    private float followSpeed = 5f;

    private Vector3 offset;

    void Start()
    {
        offset = transform.position - playerTransform.position;
    }


    void LateUpdate()
    {
        Vector3 targetPosition = playerTransform.position + offset;

        transform.position = Vector3.Lerp(transform.position, targetPosition, followSpeed * Time.deltaTime);

        transform.LookAt(playerTransform);
    }
}
